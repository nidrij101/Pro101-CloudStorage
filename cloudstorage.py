import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJ1s__NTqKtAJYMrIcbRHky8FqpX5u4H3xTfEmvY_wmLNtxvPTirFG9oUrGxME0Z20RLixkUR92on91O49fOpYalj8TNhfv33ZhLZcM8ULIm-Zwo6RRNO97DB4iYZVodtfwYl2E6Rso'
    transferData = TransferData(access_token)

    file_from = 'sample.txt'
    file_to = '/C101-Cloud Storage/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    print('Run has been successful...')

if __name__ == '__main__':
    main()

# f = open(file_from, 'rb')