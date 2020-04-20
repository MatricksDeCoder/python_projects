# Importing urllib.request
import urllib.request
# Importing io for encoding
import io

# Function to get robots.txt file
def get_robots_txt( url ):
    if url.endswith( '/' ):
        path = url
    else:
        path = url + "/"
    req = urllib.request.urlopen( path + "robots.txt", data = None )

    data = io.TextIOWrapper( req, encoding = 'utf­8' )
    print("Robots.txt done!")
    return data.read()