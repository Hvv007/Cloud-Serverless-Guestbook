terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  token     = local.token
  cloud_id  = local.cloud_id
  folder_id = local.folder_id
  zone      = local.zone
}


locals {
  token     = "y0_AgAAAAAjBSgkAATuwQAAAADZ3-t27FABVNeiRpmqq_2MkCe-wNnCGMU"
  cloud_id  = "b1grumk416bgtrc0ufut"
  folder_id = "b1gsb5ms5h345hauld53"
  zone      = "ru-central1-a"
}
