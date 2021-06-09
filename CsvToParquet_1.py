def connect_azure_blob(storage_account_name, blob_storage, storage_account_key, container_name, folder_name, file_type):
    storage_account_name = storage_account_name,
    blob_storage = blob_storage,
    storage_account_key = storage_account_key,
    container_name = container_name,
    folder_name = folder_name,
    file_type = file_type

    file_location = "wasbs://" + str(container_name) + "@" + str(storage_account_name) + ".blob.core.windows.net/" + str(folder_name)

    tempDir = "wasbs://" + str(container_name) + "@" + str(storage_account_name) + ".blob.core.windows.net/tempDir"
    #spark.conf.set("fs.azure.account.key." + storage_account_name + ".blob.core.windows.net", storage_account_key)
    #dbutils.fs.ls(file_location)
    print(file_location)
    print(tempDir)