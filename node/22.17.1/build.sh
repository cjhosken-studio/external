VERSION=$(basename "$(dirname "$0")")
SOURCE_URL="https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3"
TAR_FILE="install.sh"
NVM_DIR=$REZ_BUILD_INSTALL_PATH


if [ ! -f "$TAR_FILE" ]; then
    echo "Downloading $TAR_FILE..."
    wget $SOURCE_URL/$TAR_FILE -O $TAR_FILE
else
    echo "$TAR_FILE already exists, skipping download."
fi

sh $TAR_FILE

source $NVM_DIR/nvm.sh && nvm install $VERSION
node -v
nvm current
npm -v