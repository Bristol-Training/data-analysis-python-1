
import morse

message = "sos we have hit an iceberg"

code = morse.encode(message)
decode = morse.decode(code)

print(message == decode)
