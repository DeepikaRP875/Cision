import subprocess

# Step 2: Fetch the file content
try:
    with open('test_content.txt', 'r') as file:
        content = file.read()
        print(f"Original Content: {content}")

    # Step 3: Use grep to find the value 'deepika'
    grep_result = subprocess.run(['grep', '-o', 'deepika', 'test_content.txt'], capture_output=True, text=True)
    if grep_result.returncode != 0:
        print("The word 'deepika' was not found in the file.")
    else:
        print(f"Grep Result: {grep_result.stdout.strip()}")

        # Step 4: Use tr to delete vowels in 'deepika'
        tr_result = subprocess.run(f"echo {grep_result.stdout.strip()} | tr -d 'eiou'", capture_output=True, text=True, shell=True)
        print(f"Tr Result: {tr_result.stdout.strip()}")

        # Replace 'deepika' with the result of tr in the original content
        modified_content = content.replace('deepika', tr_result.stdout.strip())

        # Step 5: Append 'senior devsecops engineer' only once on the same line
        final_content = f"{modified_content.strip()} senior devsecops engineer"

        # Save the final result back to the file
        with open('test_content.txt', 'w') as file:
            file.write(final_content)

        # Print the final content of the file
        with open('test_content.txt', 'r') as file:
            final_content = file.read()
            print(f"Final Content: {final_content}")

except FileNotFoundError:
    print("The file 'test_content.txt' was not found. Please make sure the file exists in the current directory.")