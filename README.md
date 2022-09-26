# generate_download_signed_url


Signed GCS URL is useful in many scenarios. However, all the google's sample python code require us to "upload" the private
key file together with the code to cloud compute instances such as cloud functions, cloud run etc... 

In the [blog](https://yyfhust.github.io/2022/09/20/How-to-sign-GCS-URL-in-Cloud-hosted-instances.html): , I investigated the reasons why private key file is required in sample implementations and how to get rid of key files and 
sign GCS URL in the cloud run / functions ... 



