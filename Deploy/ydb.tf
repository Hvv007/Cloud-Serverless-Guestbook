locals {
  database_name = "guestbook-database"
}

resource "yandex_ydb_database_serverless" "guestbook_db" {
  name      = local.database_name
  folder_id = local.folder_id
}

output "guestbook_database_document_api_endpoint" {
  value = yandex_ydb_database_serverless.guestbook_db.document_api_endpoint
}

output "guestbook_database_path" {
  value = yandex_ydb_database_serverless.guestbook_db.database_path
}
