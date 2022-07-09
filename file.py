import dropbox

class transferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    accessToken = 'sl.BK914EtZRgzgxNwd_lcVjjdkR8wWLghANSHaZBr3AoKV3fL94p8HWXQR7hmqiwm9XWd6vzh13o1cmXvm3F2Eq9Q_P7Wy7NCyBp8bgapYCnwyY-b4IVpPX3FeHJn02nVZFISEEmCE0e9d'
    transferdata = transferData(accessToken)

    file_from = input('Enter the file which you want to be the source')

    file_to = input('Enter the file which you want the source file to go to')

    transferdata.upload_file(file_from, file_to)
    print("The file has been successfully transferred!")

if __name__ == '__main__': 
    main()

