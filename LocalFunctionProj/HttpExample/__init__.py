import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    zip = req.params.get('zip')
    state = req.params.get('state')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    
    if name:
        return func.HttpResponse(f"Hello {name}!")
    if zip:
        if zip =='94530':
            return func.HttpResponse("400")
        else: 
            return func.HttpResponse(f"Hello {zip}!")

    if state:
        if state =='NM':
            return func.HttpResponse("325")
        if state =='CA':
            return func.HttpResponse("467")
        if state =='TX':
            return func.HttpResponse("289")        
        else: 
            return func.HttpResponse("173")

    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
