locals {
  service_account_name = "guestbook-service-acc"
}

resource "yandex_iam_service_account" "guestbook_api_service_account" {
  name        = "${local.service_account_name}-${local.folder_id}"
  description = "Service account to call guestbook container and guestbook-database"
}

resource "yandex_iam_service_account_static_access_key" "guestbook_api_service_account_static_key" {
  service_account_id = yandex_iam_service_account.guestbook_api_service_account.id
}

output "guestbook_api_service_account_id" {
  value = yandex_iam_service_account.guestbook_api_service_account.id
}

output "aws_access_key_id" {
  value = yandex_iam_service_account_static_access_key.guestbook_api_service_account_static_key.access_key
}

output "aws_private_key" {
  value = yandex_iam_service_account_static_access_key.guestbook_api_service_account_static_key.secret_key
  sensitive = true
}
