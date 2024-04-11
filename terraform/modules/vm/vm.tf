resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_B1s"
  admin_username      = "adminuser"
  network_interface_ids = [azurerm_network_interface.test.id,]
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDdpe+2BeFyEG4HLde2VtLnf/xWpfb3Xk0EGGNNK8BVhF3hUzsON+ILfHwlYdsnMIJl+xCVW9YTWYbNIriGyKIBHbTNXh3KZ70iHLDRjgkwsnzRMeSTkARSxgV/ctSpg48DJvxMhyfmVwWLDw2LMeuXiC1cJ1OvrCXSGjM+APJt4dRBMBaMWXc4IdkgJBZBbwuDbRdPcOC/6RpujqB2NgxMDsqj0giI2qnewLr/GF98Ru4QboS/SrnPuXlpQBumP0A65GGTM4dajZvjkt2uVA7DHwSFMScxTq2f3oh/wNB8uSb4cs4StPWiWwcNktXIfWEMm9iQrDomdawW0ojqdY2GVpW+E3tOK1qni1LoBgJNOEjoUg1grN88uDMryNsmfYUpzymBywGh0W54d2EycxrfLpIDsKlvkEn1AWMRLEmAw7jgQhwLznflGMuGt+k9y5ZWVpjoXVSb5REhRwF/EhM/VkfFaB+A+Fr7GUKSdt5TYPSjy0YbBixi4Pob3TUrv0s= vinaya@SandboxHost-638453415541757999"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
