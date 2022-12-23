import requests
import looker_sdk
from looker_sdk import models
import os

os.environ["LOOKERSDK_BASE_URL"] = "https://tecnomotum.cloud.looker.com/"
os.environ["LOOKERSDK_API_VERSION"] = "4.0"
os.environ["LOOKERSDK_VERIFY_SSL"] = "true"
os.environ["LOOKERSDK_TIMEOUT"] = "120"
os.environ["LOOKERSDK_CLIENT_ID"] = "Y5TxKNc5tsH43m6x8dbH"
os.environ["LOOKERSDK_CLIENT_SECRET"] = "yw5xH7Y5HDF3wdSRCSDj9vWr"

sdk = looker_sdk.init40()

# response = sdk.board(board_id="11")

# get look, here look id 39
my_look = sdk.look("39")

# get query id for look
my_query = my_look.query


my_query = {'looker_test.Count': "=2"}


# --------------------------------------
query = sdk.look(look_id="39").query
print(query.fields)
# CREATE NEW QUERY AND ADD A FILTER

new_query = sdk.create_query(body=models.WriteQuery(
 model="alerts_sample_training", view=query.view,
 fields=query.fields,
 filters={'looker_test.count': '2', 'looker_test.name': 'Demasiado tiempo detenido (56 minutos)'}))

# UPDATE LOOK WITH NEW QUERY ID
print(new_query)
sdk.update_look(look_id="39", body=models.WriteLookWithQuery(
    query_id=new_query.id))

# RUN LOOK

result = sdk.run_look(look_id="39", result_format="csv")

# print(result)


# def update_query_filters(api_query, changes):

#     # Get the JSON version of the query
#     query = api_query.__dict__
#    # In order to create a new query, read_only fields need to be removed
#    # Filter config also needs to be removed otherwise it will override the filter options in the ui
#     read_only_fields = [
#         "Y5TxKNc5tsH43m6x8dbH",
#         "yw5xH7Y5HDF3wdSRCSDj9vWr",
#         "slug",
#         "share_url",
#         "https://tecnomotum.cloud.looker.com/",
#         "expanded_share_url",
#         "has_table_calculations",
#         "can",
#         "filter_config"
#     ]

#     for field in read_only_fields:
#         if field in query:
#             query.pop(field)
#     # Extract the filters from the query
#     filters = query['filters']
#     # the parameter 'changes' is a dictionary of keys: new_values so we update the filters dictionary

#     filters.update(changes)
#     # Update the query dictionary with the new filters

#     query.update({"filters": filters})
#     # Returns a JSON object ready to create a new query

#     return query

# update_query_filters("5303",)
