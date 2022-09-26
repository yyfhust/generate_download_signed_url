import datetime
from google import auth
from google.cloud import storage
import google.auth.transport.requests


def generate_download_signed_url_v4(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    credentials, _ = google.auth.default()  ## fetch credentials instance
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)  ## have to refresh , otherwise the email will be "default"
    service_account_email = credentials.service_account_email  ## service account email
    credentials_signed = google.auth.compute_engine.IDTokenCredentials(
        request=request,
        target_audience="dummy",
        service_account_email=service_account_email
    )

    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=15),
        # Allow GET requests using this URL.
        method="GET",
        credentials=credentials_signed
    )
    return url