country = "India"
prime_minister = "Narendra Modi"

def country_details():
    country = "USA"
    army_count = "15 lakhs"
    
    def country_secondary():
        prime_minister = "Trump"
        operation = "Sindoor"
        print(f"My country is {country}, our army count is {army_count}, our Prime Minister is {prime_minister}, proud of India operation {operation}.")
        return operation
    
    result = country_secondary()
    return result

operation = country_details()
army_count = "12 lakhs"

print(f"My country is {country}, our army count is {army_count}, our Prime Minister is {prime_minister},We are  proud of operation {operation}.")
