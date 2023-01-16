locals {
  website_gateway_name = "guestbook-website-gateway"
}

resource "yandex_api_gateway" "guestbook_website_gateway" {
  name      = local.website_gateway_name
  folder_id = local.folder_id
  spec      = file("../Frontend/openapi.yaml")
}

output "guestbook_website_gateway_domain" {
  value = "https://${yandex_api_gateway.guestbook_website_gateway.domain}"
}
