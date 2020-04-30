# spoticlean
## Delete Spotify playlists using RegEx

> Note: Spotify's architecture does not allow deleting playlists, only unfollowing playlists. [More information about working with playlists can be found here](https://developer.spotify.com/documentation/general/guides/working-with-playlists/).
## Installation 

`$ pip install spoticlean`

## Usage 

`$ spoticlean --regex <RegEx String> --token <Spotify Bearer Token>`

[You can generate a Spotify Bearer Token here](https://developer.spotify.com/console/delete-playlist-followers/)

## Example 

`$ spoticlean --regex "pl..s. del.t. .e" --token BQCD-kZJPoh3ejcbdoraKM1m07coOTlhs0Zc6U93cn6EF_QxKeTncRPxh0i-fT3e46EDFkTz5Dd1UCXANrwv-LBZkKYAaR37lDJcga0NHC5A5dmCcj4nmaLhEx4Yf3tLNYX-1fue8TnudeUgtiCtXugVKjePdrKLFNUBoZp1jE_3VFhW_Eh13fjdoeklpcRAxiEmKgHSlNnwqBuWS_ZUWkwuISziFhna-Xg-g8iFnESbWeori5Dl3WA4Atd67RSJtW9YSAzKRIp9ew`

```
Found the following playlists:

    - please delete me
    - plooss delatx ye

Press Enter to delete playlists
```


