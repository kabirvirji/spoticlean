from setuptools import setup, find_packages

setup(
	name='spoticlean',
	version='0.0.1',
	license="MIT",
	description='Delete Spotify playlists using RegEx',
	url="https://github.com/kabirvirji/spoticlean",
    packages=find_packages(),
    install_requires=[],
    python_requires = ">= 3.4",
    author="Kabir Virji",
    author_email="kabirvirji@gmail.com",
)
