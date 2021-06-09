

def connect_azure_blob(storage_account_name, blob_storage, storage_account_key, container_name, folder_name, file_type, input):


    file_location = "wasbs://" + container_name + "@" + storage_account_name + ".blob.core.windows.net/" + folder_name

    #tempDir = "wasbs://" + container_name + "@" + storage_account_name + ".blob.core.windows.net/tempDir"

    #spark.conf.set("fs.azure.account.key." + storage_account_name + ".blob.core.windows.net", storage_account_key)
    #dbutils.fs.ls(file_location)
    #spark.conf.set('fs.azure.account.key.' + storage_account_name + '.blob.core.windows.net', storage_account_access_key)

    sparkConfig = 'fs.azure.account.key.' + storage_account_name + '.blob.core.windows.net' + storage_account_key

    if input == 1:
        return file_location
    else:
        return sparkConfig
