
docker run --rm -v $PWD:/local \
    openapitools/openapi-generator-cli generate \
    -i https://api.ynab.com/papi/open_api_spec.yaml \
    -g python \
    -o /local



./ynabtools/main.py debug --test getbudget --parameter budget_id=b0712566-78fc-40ab-8c32-d31b10a727e0
./ynabtools/main.py backup
./ynabtools/main.py export --pickle backup/20241231/d4d0205b-11c9-4c9a-92c2-4ab17f0d1cdb.pkl