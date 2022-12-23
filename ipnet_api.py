import looker_sdk
from looker_sdk import models
import os
import json

os.environ["LOOKERSDK_BASE_URL"] = "https://ipnet.sa.looker.com/"
os.environ["LOOKERSDK_API_VERSION"] = "4.0"
os.environ["LOOKERSDK_VERIFY_SSL"] = "true"
os.environ["LOOKERSDK_TIMEOUT"] = "120"
os.environ["LOOKERSDK_CLIENT_ID"] = "XGHFmgk6JJhrDdmk5Z9D"
os.environ["LOOKERSDK_CLIENT_SECRET"] = "yqDXDTZ3vxqTSVHhwRYGDH73"

sdk = looker_sdk.init40()


dashboard_id = "204"
# Pegando os filtros desse Dash
dominio_user = "ipnetsolucoes.com.br"

response = sdk.update_dashboard_filter(
    dashboard_filter_id="315",
    body=models.WriteDashboardFilter(
        name="Dominio",
        title="Dominio",
        type="field_filter",
        default_value=dominio_user,
        model="adoption",
        explore="reports_customer_gmail",
        dimension="reports_customer_gmail.dominio",
        row=0,
        allow_multiple_values='false',
        required='false',
        ui_config={
            "type": "checkboxes",
            "display": "popover"
        }
    ))


