import graphtaint as g

# Define a helper function to handle exceptions and print results
def handle_exception(method, inputs):
    try:
        result = method(*inputs)
        print(result)
    except Exception as e:
        print(str(e))

# Fuzz.py performs fuzzing on 5 methods contained in the graphtaint.py file

# Method 1 - getYAMLFiles()
print('--------------------------------------')
print('Fuzzing method getYAMLFiles()')
print('--------------------------------------')

input1 = [2, 'Hello World!', [7]]

for inp in input1:
    handle_exception(g.getYAMLFiles, [inp])


# Method 2 - constructHelmString()
print('\n')
print('--------------------------------------')
print('Fuzzing method constructHelmString()')
print('--------------------------------------')
input2 = [(1, "two", 3), None, "string"]

for inp in input2:
    handle_exception(g.constructHelmString, [inp])

# Method 3 - getHelmTemplateContent()
print('\n')
print('--------------------------------------')
print('Fuzzing method getHelmTemplateContent()')
print('--------------------------------------')
input3 = ['random/directory', None, (7, 2)]

for inp in input3:
    handle_exception(g.getHelmTemplateContent, [inp])

# Method 4 - getMatchingTemplates()
print('\n')
print('--------------------------------------')
print('Fuzzing method getMatchingTemplates()')
print('--------------------------------------')
input4 = [0, "String", None]
input4_2 = [("tu", "ple"), "🐵 🙈 🙉 🙊", None]

for i in range(len(input4)):
    handle_exception(g.getMatchingTemplates, [input4[i], input4_2[i]])

# Method 5 - getValidTaints()
print('\n')
print('--------------------------------------')
print('Fuzzing method getValidTaints()')
print('--------------------------------------')
input5 = ["Not a List", ['invalid list', 2], None]

for inp in input5:
    handle_exception(g.getValidTaints, [inp])
