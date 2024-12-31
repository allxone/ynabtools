#!/usr/bin/env python

import os
import csv
import argparse
import openapi_client
import pickle
from datetime import datetime

BASE_URL = "https://api.ynab.com/v1"


class YNABtools:
    @staticmethod
    def parse_arguments():
        def parse_key_value(value):
            key, val = value.split("=")
            return key, val

        parser = argparse.ArgumentParser(description="YNAB Tools")
        parser.add_argument(
            "--host",
            required=False,
            default=BASE_URL,
        )
        parser.add_argument(
            "--access_token",
            required=False,
            default=os.environ["YNAB_APIKEY"],
            help="If omitted the YNAB api key is read from the YNAB_APIKEY environment variable",
        )
        subparsers = parser.add_subparsers(dest="command", required=True)

        # Export Budget subparser
        export_parser = subparsers.add_parser("export")
        export_parser.add_argument(
            "--path",
            type=str,
            default=os.path.join("export", datetime.now().strftime("%Y%m%d")),
        )
        export_group = export_parser.add_mutually_exclusive_group(required=True)
        export_group.add_argument("--budget_id", type=str, help="Budget ID")
        export_group.add_argument(
            "--pickle_path",
            type=str,
            help="Path del file Pickle prodotto dal metodo 'backup'",
        )

        # Backup subparser
        backup_parser = subparsers.add_parser("backup")
        backup_parser.add_argument(
            "--path",
            type=str,
            default=os.path.join("backup", datetime.now().strftime("%Y%m%d")),
        )

        # Debug subparser
        debug_parser = subparsers.add_parser("debug")
        debug_parser.add_argument(
            "--test",
            choices=["getuser", "getbudgets", "getbudget"],
            default="getuser",
        )
        debug_parser.add_argument(
            "--parameter",
            type=parse_key_value,
            action="append",
            help="Specify a key=value pair",
        )
        return parser.parse_args()

    def __init__(self, args):
        self.args = args
        self.configuration = openapi_client.Configuration(
            host=args.host,
            access_token=args.access_token,
        )

    def debug(self, test, parameters={}):
        if test == "getuser":
            with openapi_client.ApiClient(self.configuration) as api_client:
                api_instance = openapi_client.UserApi(api_client)
                user = api_instance.get_user()
                print(user.data)
        elif test == "getbudgets":
            with openapi_client.ApiClient(self.configuration) as api_client:
                api_instance = openapi_client.BudgetsApi(api_client)
                budgets = api_instance.get_budgets()
                print(budgets.data)
        elif test == "getbudget":
            with openapi_client.ApiClient(self.configuration) as api_client:
                api_instance = openapi_client.BudgetsApi(api_client)
                budget = api_instance.get_budget_by_id(**parameters)
                print(budgets.data)

        else:
            raise NotImplemented(test)

    def get_budget_by_id(self, budget_id) -> openapi_client.BudgetDetailResponse:
        with openapi_client.ApiClient(self.configuration) as api_client:
            api_instance = openapi_client.BudgetsApi(api_client)
            return api_instance.get_budget_by_id(budget_id)

    def get_budget_from_pickle(
        self, pickle_path
    ) -> openapi_client.BudgetDetailResponse:
        with open(pickle_path, "rb") as pickle_file:
            return pickle.load(pickle_file)

    def export_budget(self, budget: openapi_client.BudgetDetailResponse, path):
        myBudget = budget.data.budget
        path = os.path.join(path, myBudget.id)

        # Verify output folder
        if not os.path.exists(path):
            os.makedirs(path)

        self._export_budget(myBudget, path, "budget.csv")
        self._export_items(myBudget.categories, path, "categories.csv")
        self._export_items(myBudget.category_groups, path, "category_groups.csv")
        self._export_items(myBudget.accounts, path, "accounts.csv")
        self._export_items(myBudget.months, path, "months.csv")
        self._export_items(myBudget.payees, path, "payees.csv")
        self._export_items(myBudget.payee_locations, path, "payee_locations.csv")
        self._export_items(myBudget.transactions, path, "transactions.csv")
        self._export_items(myBudget.subtransactions, path, "subtransactions.csv")
        self._export_items(
            myBudget.scheduled_transactions, path, "scheduled_transactions.csv"
        )
        self._export_items(
            myBudget.scheduled_subtransactions, path, "scheduled_subtransactions.csv"
        )

    def _normalize_string(self, value: str) -> str:
        if isinstance(value, str):
            # Rimuovi ritorni a capo, tabulazioni e spazi extra
            return value.replace("\n", " ").replace("\r", "").strip()
        return value

    def _export_budget(self, budget, path, file_name):
        output_file = os.path.join(path, file_name)

        with open(output_file, mode="w") as file:
            budget_model = budget.model_dump(
                exclude={
                    "categories",
                    "category_groups",
                    "accounts",
                    "months",
                    "payees",
                    "payee_locations",
                    "transactions",
                    "subtransactions",
                    "scheduled_transactions",
                    "scheduled_subtransactions",
                }
            )
            # Estrai le intestazioni
            fieldnames = budget_model.keys()

            # Crea il writer per il CSV
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Scrivere l'intestazione nel file
            writer.writeheader()

            # Scrivere tutte le righe, usando il metodo .dict() per ciascun oggetto
            normalized_data = {
                key: self._normalize_string(value)
                for key, value in budget_model.items()
            }
            writer.writerow(normalized_data)  # Converte l'oggetto in un dizionario

    def _export_items(self, items, path, file_name):
        if not items:
            print(f"\tskipping {file_name}")
            return

        output_file = os.path.join(path, file_name)
        with open(output_file, mode="w") as file:
            # Estrai le intestazioni
            fieldnames = items[0].to_dict().keys()

            # Crea il writer per il CSV
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Scrivere l'intestazione nel file
            writer.writeheader()

            # Scrivere tutte le righe, usando il metodo .dict() per ciascun oggetto
            for item in items:
                normalized_data = {
                    key: self._normalize_string(value)
                    for key, value in item.to_dict().items()
                }
                writer.writerow(normalized_data)  # Converte l'oggetto in un dizionario

    def backup(self, path, skipExport=False):
        # Verify output folder
        if not os.path.exists(path):
            os.makedirs(path)

        # Backup every budget
        with openapi_client.ApiClient(self.configuration) as api_client:
            api_instance = openapi_client.BudgetsApi(api_client)
            budgets = api_instance.get_budgets()
            for budgetSummary in budgets.data.budgets:
                print(f"Backup of {budgetSummary.name} ({budgetSummary.id})")
                budget = api_instance.get_budget_by_id(budgetSummary.id)
                print(f"\tdownloaded")

                # Backup
                backup_file = os.path.join(path, f"{budgetSummary.id}.pkl")
                with open(backup_file, "wb") as pickle_file:
                    pickle.dump(budget, pickle_file)
                    print(f"\twritten to {backup_file}")

                # Verify
                with open(backup_file, "rb") as pickle_file:
                    restore = pickle.load(pickle_file)
                    if restore == budget:
                        print(f"\tverified from {backup_file}")
                    else:
                        raise ValueError("Invalid restore")

                # Export
                if not skipExport:
                    self.export_budget(budget, path)


def main():

    # Parse the command line arguments
    args = YNABtools.parse_arguments()

    # Invoke application
    ynab = YNABtools(args)

    if args.command == "debug":
        params = dict(args.parameter) if args.parameter else {}
        ynab.debug(args.test, params)
    elif args.command == "backup":
        ynab.backup(args.path)
    elif args.command == "export":
        # Get Budget
        if args.budget_id:
            budget = ynab.get_budget_by_id(args.budget_id)
        elif args.pickle_path:
            budget = ynab.get_budget_from_pickle(args.pickle_path)
        else:
            raise NotImplementedError()

        # Export Budget
        ynab.export_budget(budget, args.path)
    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
