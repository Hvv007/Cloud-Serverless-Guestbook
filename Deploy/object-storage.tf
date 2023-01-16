locals {
  website_bucket_name = "guestbook-website"
}

resource "yandex_storage_bucket" "guestbook_website_bucket" {
  bucket     = "${local.website_bucket_name}-${local.folder_id}"
  access_key = yandex_iam_service_account_static_access_key.guestbook_api_service_account_static_key.access_key
  secret_key = yandex_iam_service_account_static_access_key.guestbook_api_service_account_static_key.secret_key
}

output "guestbook_website_bucket" {
  value = yandex_storage_bucket.guestbook_website_bucket.bucket
}