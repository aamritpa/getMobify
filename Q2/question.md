# Question 2 (6 points)

Create a program that can transform input text from any of camelCase, PascalCase, snake_case or kebab-case into any one of the others, based on command-line arguments. Input and command-line processing should be handled in one language, and output to the other case should be handled in at least one other language.

The output format will be separated with a command line switch named “case”, with allowed values of “camelCase”, “PascalCase”, “snake_case” or “kebab-case”, e.g `./myprogram -case snake_case < input_file`. Input will be a single line of text on standard input containing a sample in one of camelCase, PascalCase, snake_case or kebab-case, output should also be a single line in the desired case on standard output.