import sys
import tkinter as tk
from tkinter import simpledialog, messagebox


# 3rd Party
import requests
import pandas as pd
from typing import Tuple

JWT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpxQlVSc09YM1ItTzZxTFRBQklrOSJ9.eyJodHRwczovL2F6dXJlYWQjb2lkIjoiN2Y1YjA2OTEtZjEwMC00OTljLWEzNzQtN2E5ZTU1NWZmMzRhIiwiaHR0cHM6Ly9henVyZWFkI2FkX2FjY2Vzc190b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0p1YjI1alpTSTZJblEzYURONVJGVXlXRnB5Vm5KWU1YbEVhWFJCWld4NmNIVkJhbUpOV0V0UlNuTTJjM0kwWDBoRmJWRWlMQ0poYkdjaU9pSlNVekkxTmlJc0luZzFkQ0k2SW01UGJ6TmFSSEpQUkZoRlN6RnFTMWRvV0hOc1NGSmZTMWhGWnlJc0ltdHBaQ0k2SW01UGJ6TmFSSEpQUkZoRlN6RnFTMWRvV0hOc1NGSmZTMWhGWnlKOS5leUpoZFdRaU9pSXdNREF3TURBd015MHdNREF3TFRBd01EQXRZekF3TUMwd01EQXdNREF3TURBd01EQWlMQ0pwYzNNaU9pSm9kSFJ3Y3pvdkwzTjBjeTUzYVc1a2IzZHpMbTVsZEM5bVlXTmhZek5qTkMxbE1tRTFMVFF5TlRjdFlXWTNOaTB5TURWak9HRTRNakZrWkdJdklpd2lhV0YwSWpveE5qSTBNRE15TkRneExDSnVZbVlpT2pFMk1qUXdNekkwT0RFc0ltVjRjQ0k2TVRZeU5EQXpOak00TVN3aVlXTmpkQ0k2TUN3aVlXTnlJam9pTVNJc0ltRmpjbk1pT2xzaWRYSnVPblZ6WlhJNmNtVm5hWE4wWlhKelpXTjFjbWwwZVdsdVptOGlMQ0oxY200NmJXbGpjbTl6YjJaME9uSmxjVEVpTENKMWNtNDZiV2xqY205emIyWjBPbkpsY1RJaUxDSjFjbTQ2YldsamNtOXpiMlowT25KbGNUTWlMQ0pqTVNJc0ltTXlJaXdpWXpNaUxDSmpOQ0lzSW1NMUlpd2lZellpTENKak55SXNJbU00SWl3aVl6a2lMQ0pqTVRBaUxDSmpNVEVpTENKak1USWlMQ0pqTVRNaUxDSmpNVFFpTENKak1UVWlMQ0pqTVRZaUxDSmpNVGNpTENKak1UZ2lMQ0pqTVRraUxDSmpNakFpTENKak1qRWlMQ0pqTWpJaUxDSmpNak1pTENKak1qUWlMQ0pqTWpVaVhTd2lZV2x2SWpvaVJUSmFaMWxDUkhrdmRrVnlWVkJJTlhBNGNrUlFhMjB6TURWT1MyUjVja3QyVVhWYWRVaDBjRkoxZDFweE5XSm1RbTFqUVNJc0ltRnRjaUk2V3lKd2QyUWlMQ0p5YzJFaVhTd2lZWEJ3WDJScGMzQnNZWGx1WVcxbElqb2lNMDB0UTFKVFRFSk1TeTFCZFhSb01FWmxaR1Z5WVhScGIyNHRibTl1Y0hKdlpDMWhjSEFpTENKaGNIQnBaQ0k2SWpRME5URTFORGRtTFRCalpXSXRORGM0T1MwNE1HWTFMVE0zWWpjeU9UTTJaVEkxWXlJc0ltRndjR2xrWVdOeUlqb2lNU0lzSW1SbGRtbGpaV2xrSWpvaVpXWmtZamszT1dZdFlUQTJaQzAwTW1WakxXSXdabU10T1RjeE9XSTRPRGN6WldKa0lpd2labUZ0YVd4NVgyNWhiV1VpT2lKSGRXTnJaVzVpWlhKblpYSWlMQ0puYVhabGJsOXVZVzFsSWpvaVFXeGxlR0Z1WkdWeUlpd2lhV1IwZVhBaU9pSjFjMlZ5SWl3aWFYQmhaR1J5SWpvaU1qUXVNVEU0TGpNNExqVXpJaXdpYm1GdFpTSTZJa0ZzWlhoaGJtUmxjaUJIZFdOclpXNWlaWEpuWlhJaUxDSnZhV1FpT2lJM1pqVmlNRFk1TVMxbU1UQXdMVFE1T1dNdFlUTTNOQzAzWVRsbE5UVTFabVl6TkdFaUxDSnZibkJ5WlcxZmMybGtJam9pVXkweExUVXRNakV0TVRFeU16VTJNVGswTlMweU1EYzNPREEyTWpBNUxURTRNREUyTnpRMU16RXROekEyTURJMElpd2ljR3hoZEdZaU9pSXpJaXdpY0hWcFpDSTZJakV3TURNeU1EQXdNemMxTWtZMk9URWlMQ0p5YUNJNklqQXVRVkpOUVhoTlVFc3RjVmhwVmpCTGRtUnBRbU5wYjBsa01qTTVWVlZWVkhKRVNXeElaMUJWTTNSNWF6STBiSGRVUVVWQkxpSXNJbk5qY0NJNklrUnBjbVZqZEc5eWVTNUJZMk5sYzNOQmMxVnpaWEl1UVd4c0lFUnBjbVZqZEc5eWVTNVNaV0ZrTGtGc2JDQmxiV0ZwYkNCd2NtOW1hV3hsSUZWelpYSXVVbVZoWkNCVmMyVnlMbEpsWVdRdVFXeHNJRzl3Wlc1cFpDSXNJbk5wWjI1cGJsOXpkR0YwWlNJNld5SmtkbU5mYlc1blpDSXNJbVIyWTE5a2JXcGtJaXdpYTIxemFTSmRMQ0p6ZFdJaU9pSm5Ta3R3WDFjMU4zcFNjemRMUVRWYVMxSmZOUzAxU0d4WFJXUllhblJNYXpZd2FXeEhaRVF3VEd4Rklpd2lkR1Z1WVc1MFgzSmxaMmx2Ymw5elkyOXdaU0k2SWs1Qklpd2lkR2xrSWpvaVptRmpZV016WXpRdFpUSmhOUzAwTWpVM0xXRm1Oell0TWpBMVl6aGhPREl4WkdSaUlpd2lkVzVwY1hWbFgyNWhiV1VpT2lKQk9FdzFWMXBhUUcxdGJTNWpiMjBpTENKMWNHNGlPaUpCT0V3MVYxcGFRRzF0YlM1amIyMGlMQ0oxZEdraU9pSmZTakZ4YW5CYVRISkZRM1JhTUVSME56UjNZa0ZCSWl3aWRtVnlJam9pTVM0d0lpd2lkMmxrY3lJNld5SmlOemxtWW1ZMFpDMHpaV1k1TFRRMk9Ea3RPREUwTXkwM05tSXhPVFJsT0RVMU1Ea2lYU3dpZUcxelgzTjBJanA3SW5OMVlpSTZJa3AwYlU1bU1FUjNOemxzWjJKUk0xOTBTSFExUW5kUVFXbFdVWGw1TkVobk1tbHRjWGcyYlcwMGVVMGlmU3dpZUcxelgzUmpaSFFpT2pFek9ETTJPRFl4TkRSOS5oRUN3aTFjWTdaZi1yVEVheFF6NDBFZ0FNVjNVc3JzLWtOb0hzaUpKWHhzbUM2WHQxRDlXc1BKczFTRDBvdUtqQVJEZVJsaElqWWJVYVFWZDNmaHRsUDZ2WlVtR3hXdDljR1Z0Mk9MOGpGVWdpRlRCQjZ1bG1sZ1RyYXpUNkoyUXJhYTdFR19qdDVVaU9IVGNuMGpjZVpYUzRjYVdvNjF0WkN5TEVnNDRqYkJaM0V5NWd5MHpaM0FwTTlMQk1WQzFkU0xuSnEyaTNGZGVtYXJXMjRiY09mNEFoNXZ4dUlLS0dOMDUybWR3YkROZEFkZzBfcjZxQWNiNk1QeElDQnZrR3pPbGo4OWgwUHBmb1FMRGQ1eFdGYk5BaEVrdXc4cU9kNmNCUFRWVmMzSlZTYnQyNk9VUmhiOU1SWmNwU2FzVm1UbEh5S2xTRUVJaTNiWU1GWVBLdmciLCJodHRwczovL2F6dXJlYWQjdXBuIjoiQThMNVdaWkBtbW0uY29tIiwiaHR0cHM6Ly9henVyZWFkI2FkX2dyb3VwcyI6IldXLUFXUy1DUlNMQkxLMzUtQWxsLU1hbmFnZXIjV1ctQVdTLUNSU0xCTEszNi1BbGwtTWFuYWdlciIsImlzcyI6Imh0dHBzOi8vbW1tLXFhLmF1dGgwLmNvbS8iLCJzdWIiOiJ3YWFkfEp0bU5mMER3NzlsZ2JRM190SHQ1QndQQWlWUXl5NEhnMmltcXg2bW00eU0iLCJhdWQiOlsiaHR0cHM6Ly9vemFyay5xYS5vemFyay5jbGQuM20uY29tIiwiaHR0cHM6Ly9tbW0tcWEuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyNDAzMjc4MywiZXhwIjoxNjI0MTE5MTgzLCJhenAiOiJidTlFcWp5RUJyNjNZNm14ODhWdkpvZW1GbEZUYXVaYiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.E5mrG-DHJWK9EkL2ud40jM8NhYFaotV3c_1bYBsl03dr52-mBnnb9iihjvTB58EQ6JuMzXZYU3v9-4J59gZZFtn67TlaIpKgC3xMwcNXUtDRV_Qh36mH-YPQE1LqzjMkxsMaBHIz0xiy5_HyKYkI1DbuUqzhfechg4Oe9h3YBxLlTz8f_6gMStE0lrByiCJqqb-A8xckIHJ5rMSg_Pp48Hebxqxic8LdrKmjmFjbLSh3UMAhUS0O8bjku5FuoKdGFQ82R751R-VsHT23GreredAQ1oCCVwmpMN5hxKn4uLlCzoHavrEBQ-CXSkzH1ka90HqO24wjrw5FY_bG8EVEYg"
BASE_URL = "https://ozark.qa.ozark.cld.3m.com/v0/api"

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, request):
        request.headers["authorization"] = "Bearer " + self.token
        return request

def get_df(url: str, token: str) -> Tuple[str, pd.DataFrame]:
    """
    Return the name of the moel and its dataframe
    """
    options = requests.options(url, auth=BearerAuth(token))
    if options.status_code != 200:
        raise RuntimeError(f"API at url ({url}) returned non 200: {options.text}")
    options = options.json()
    model_name = options['modelName']
    field_meta = options['fields']
    headers = list(field_meta.keys())
    def _get_data(_url, _data=None):
        if not _url:
            return None
        if _data is None:
            _data = []
        response = requests.get(_url, auth=BearerAuth(token))
        if response.status_code != 200:
            raise RuntimeError(f"API returned non 200: {response.text}")
        response = response.json()
        _data.extend([[result[header] for header in headers] for result in response['results']])
        _get_data(response["next"], _data)
        return pd.DataFrame(_data, columns=headers)
    return model_name, _get_data(url)

endpoints = [
    (f'{BASE_URL}/coastline/contracts', 'coast_line'),
    (f'{BASE_URL}/coastline/requestlots', 'coast_line'),
    (f'{BASE_URL}/coastline/gellots', 'coast_line'),
    (f'{BASE_URL}/coastline/runlots', 'coast_line'),
    (f'{BASE_URL}/coastline/toolings', 'coast_line'),
    (f'{BASE_URL}/coastline/materialchemistries', 'coast_line'),
    (f'{BASE_URL}/coastline/requestvsdtypes', 'coast_line'),
    (f'{BASE_URL}/coastline/vsdlipmaterials', 'coast_line'),
    (f'{BASE_URL}/coastline/radeliverymethods', 'coast_line'),
    (f'{BASE_URL}/coastline/applicatorbladematerials', 'coast_line'),
    (f'{BASE_URL}/coastline/applicatorsidefoaminserttypes', 'coast_line'),
    (f'{BASE_URL}/coastline/aniloxrolltypes', 'coast_line'),
    (f'{BASE_URL}/coastline/coatingrolldurometers', 'coast_line'),
    (f'{BASE_URL}/coastline/horntipwidths', 'coast_line'),
    (f'{BASE_URL}/coastline/collectionvesseltypes', 'coast_line'),
    (f'{BASE_URL}/coastline/coatingslotwidths', 'coast_line'),
    (f'{BASE_URL}/coastline/coatingdienames', 'coast_line'),

    # Mineral Firing
    (f'{BASE_URL}/mineralfiring/contracts', 'coast_line'),
    (f'{BASE_URL}/mineralfiring/requestlots', 'mineral_firing'),
    (f'{BASE_URL}/mineralfiring/runlots', 'mineral_firing'),
    (f'{BASE_URL}/mineralfiring/impregnationtypes', 'mineral_firing'),
    (f'{BASE_URL}/mineralfiring/firingmethods', 'mineral_firing'),
    (f'{BASE_URL}/mineralfiring/kilns', 'mineral_firing'),
    (f'{BASE_URL}/mineralfiring/mixingequipments', 'mineral_firing'),
    
]

try:
    for endpoint, model_namespace in endpoints:
        model_name, df = get_df(endpoint, JWT_TOKEN)
        variable = f"{model_namespace}_{model_name}"
        if variable in vars():
            messagebox.showerror(
                "Error Occured",
                "Read a model name twice for this namespace. Contact a system admin."
                f" Variable Name: {variable}")
            sys.exit(1)
        vars()[variable] = df 
except RuntimeError as e:
    application_window = tk.Tk()
    application_window.withdraw() # Hide the app window
    if e.args and "Unauthorized" not in e.args[0]:
        messagebox.showerror(
            "Error Occured",
            f"An unexpected error occured, contact a system admin.\n{e}")
        sys.exit(1)
    new_token = simpledialog.askstring(
        "Input",
        "Unauthorized - try pasting a new JWT from Ozark",
        parent=application_window)
    application_window.destroy()
    for endpoint, model_namespace in endpoints:
        model_name, df = get_df(endpoint, str(new_token))
        variable = f"{model_namespace}_{model_name}"
        if variable in vars():
            messagebox.showerror(
                "Error Occured",
                "Read a model name twice for this namespace. Contact a system admin."
                f" Variable Name: {variable}")
            sys.exit(1)
        vars()[variable] = df 

del vars()['df']
sys.exit(0)
