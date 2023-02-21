# URL Shortener App

| Collaborators                                 |
| --------------------------------------------- |
| [liambrockpy](github.com/liambrockpy) &#9758; |
| [JLP2000](github.com/JLP2000) &#9758;         |

Built with Flask, a simple URL shortener app with QR code image generation.

Running live on ...

## Technologies

- Python
- JavaScript
- Flask:
  - flask-wtf
  - flask-sqlalchemy
  - flask-migrate
  - qrcode
  - pytest
- SQLite

## Process

## Wins and Challenges

#### Wins

- Displays history of links created with removal functionality

#### Challenges

- One initial challenge we faced was if users input a URL with just the domain name, if that was retrieved from the database and used as a `href` attribute within links, it would see it as relative URL and not external. We therefore built a simple URL parser to add `http://` prefixes to URLs. As a bonus side effect, this also helped reduce possible duplicates within the database too.
- Another fun challenge was creating a recent history of links created using local storage. On first look we realised _"oh, you can only store strings, but we need to save the long and shortened url together!"_. With further reading we discovered we could stringify the data into JSON strings and just parse it back to JavaScript when we needed to display the data.