
###What is URL?
https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL

###What HTTP is?
https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

###What is Subdomain?
https://www.wpbeginner.com/glossary/subdomain/

scheme://hostname:port/path?query#fragment
http://example.com:8080/path/to/resource?param1=value1&param2=value2#fragment

##What a query is?


A query string is a component of a URL (Uniform Resource Locator) that contains data that 
is passed to a web application or server as a set of key-value pairs. The query string is 
usually located at the end of the URL and begins with a question mark "?" character, followed 
by one or more key-value pairs separated by ampersands "&". 

For example, in the URL "https://www.example.com/search?q=hello+world&category=books", 
the query string is "q=hello+world&category=books". In this case, the key-value pairs are 
"q=hello+world" and "category=books". The "q" key has the value "hello+world", 
which is the search term, and the "category" key has the value "books", which 
is the category of the search results.


Web applications use the data in the query string to dynamically generate content, filter 
search results, or perform other operations based on user 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Messagesinput. The data in the query string 
can be accessed and processed on the server-side using programming languages like PHP, 
Java, or Python, or on the client-side using JavaScript.


##What is an HTTPS request?
An HTTP (Hypertext Transfer Protocol) request is a message sent by a client (such as a web 
browser) to a web server in order to retrieve or manipulate resources, such as web pages, images, 
or other data. The request typically includes a method (such as GET or POST), a URI (Uniform 
Resource Identifier) that identifies the resource being requested, and headers that provide 
additional information about the request, such as the type of data being accepted by the client.

For example, when you enter a URL (Uniform Resource Locator) into a web browser, the browser sends 
an HTTP request to the web server specified in the URL, asking for the resource (such as a web 
page) associated with that URL. The server then responds to the request with an HTTP response, 
which typically includes the requested resource along with additional headers providing 
information about the response.


##What is HTTPS response?


An HTTP response is the message sent by a web server to a client's web browser in response to an 
HTTP request. When a web browser sends an HTTP request to a server, the server processes the 
request and sends back an HTTP response containing the requested information, usually in the form 
of HTML, images, or other resources. 

The HTTP response typically includes a status code, which indicates whether the request was successful,
 and additional metadata, such as content type and length, caching information, and cookies. 
The status code is a three-digit number that indicates the outcome of the request, such as 
"200 OK" for a successful response, "404 Not Found" for a missing resource, or "500 Internal 
Server Error" for a server-side error. The response body contains the actual content requested 
by the client, which could be an HTML page, an image file, or any other type of data.



##What are HTTP headers are?
HTTP headers are additional information that is sent between a client (such as a web browser) 
and a server when making a request or response over the Hypertext Transfer Protocol (HTTP). 

HTTP headers are used to provide metadata about the request or response, such as the type of 
data being sent, the encoding of that data, the language it is written in, and 
authentication information.

Some common HTTP headers include:

1. User-Agent: Specifies the user agent that is accessing the resource, such as the type 
of web browser or operating system being used.
2. Accept: Specifies the MIME types that are acceptable for the response.
3. Content-Type: Specifies the MIME type of the data in the body of the request or response.
4. Authorization: Provides authentication credentials for accessing a protected resource.
5. Cache-Control: Specifies caching behavior for the response.

There are many other HTTP headers, and each serves a specific purpose in helping to facilitate 
communication between clients and servers over the internet.


###What is HTTP message body
https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages


###What are web cookies?
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
