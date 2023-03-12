import logging
logging.basiciConfig(level=logging.INFO)
class WriteToFile:
    def __init__(self, filename: str, buffer_data: bytes):
        self.filename = filename
        self.buffer_data = buffer_data

    def Write(self):
        try:
            with open(self.filename, "wb") as exploit:
                exploit.write(self.buffer_data)
                print(f"Buffer successfully written to {self.filename}")
        except Exception as e:
            logging.info(f"Failed to write buffer to {self.filename}: ", str(e))

