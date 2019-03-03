param (
    [Parameter(Mandatory)][string]$Name,
    [Parameter(Mandatory)][string]$Project,
    [string]$Region = "europe-west1",
    [string]$FunctionName = "main"
)

gcloud beta functions deploy $Name --entry-point $FunctionName --runtime python37 --trigger-http --project $Project --region $Region --source ./src
