from geopy.geocoders import Nominatim

def zipcode_validation (zip_code):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    return geolocator.geocode(zip_code)

def validation_digit (zipcode_for_validation):
    if zipcode_for_validation.isdigit():
        return(zipcode_validation(zipcode_for_validation))
            
    else:
        return("Please enter a valid numeric zip code")            
    
if __name__ == '__main__':
    zipcode_probability = input("Enter zip code : ")
    
    print(validation_digit(zipcode_probability))