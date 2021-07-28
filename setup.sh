#!/bin/bash

# Sorry not sorry if this annoys you. I'm just trying to make it easy for me as I keep forgetting the 3.
echo "alias pip=pip3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.zshrc
echo "alias get-func-add='npx -q codespaces-port 7071'" >> ~/.zshrc
echo "alias get-site-add='npx -q codespaces-port 4000'" >> ~/.zshrc

export base_url=`get-site-add`
export api_url=`get-func-add`

sed -i "s|^url: \".*\"|url: \"$base_url\"|g" /workspaces/$RepositoryName/site/rad/_config.codesapce.yml
sed -i "s|^api_url: \".*\"|api_url: \"$api_url\"|g" /workspaces/$RepositoryName/site/rad/_config.codesapce.yml