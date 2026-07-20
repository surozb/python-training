
name = input("Suite name: ")
total_test = int(input("How many tests? "))
passed_count = int(input("How many passed? "))

pass_percentage = (passed_count / total_test) * 100

print(f"[{name}] {passed_count}/{total_test} passed {pass_percentage:.1f}% - {total_test - passed_count} failed") 