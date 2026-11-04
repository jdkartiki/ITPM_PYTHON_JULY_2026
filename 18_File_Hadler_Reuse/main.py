import file_handler

file_handler.write_file("18_File_Hadler_Reuse/test.txt", "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.")

print(file_handler.read_file("18_File_Hadler_Reuse/test.txt"))