#!/bin/sh

# Arguments
#--------------------
WORKSPACE=$1

# Deployment Environment
#--------------------
PROJECT_NAME=logd
SOURCE=/opt/data/hudson/$WORKSPACE/workspace
TARGET=/opt/wsgi/$WORKSPACE
EXECUTE=/opt/bin/exec-as-root

# Virtual Environment
#---------------------
VIRTUAL_ENV=/opt/apps/python/bin/virtualenv
VIRTUAL_BIN=env/bin
VIRTUAL_PY=$VIRTUAL_BIN/python

# Buildout Environment
#--------------------
BUILDOUT_BIN=bin
BUILDOUT_BOOTSTRAP="$VIRTUAL_PY bootstrap.py"
BUILDOUT_INSTALL_SERVER_DEV="$BUILDOUT_BIN/buildout -v -c integration.cfg"
BUILDOUT_INSTALL_SERVER_INT="$BUILDOUT_BIN/buildout -v -c integration.cfg"
BUILDOUT_INSTALL_SERVER_REL="$BUILDOUT_BIN/buildout -v -c production.cfg"
BUILDOUT_SETUP=$BUILDOUT_BIN/setup-app
BUILDOUT_TEST="$BUILDOUT_BIN/tests-all"
BUILDOUT_COVERAGE="$BUILDOUT_BIN/coverage"
BUILDOUT_LINT=$BUILDOUT_BIN/lint
BUILDOUT_MINIFY="$BUILDOUT_BIN/minify"

echo "*********************"
echo "***   Preparing   ***"
echo "*********************"
$VIRTUAL_ENV --no-site-packages env

echo "************************"
echo "***   Initializing   ***"
echo "************************"
$BUILDOUT_BOOTSTRAP
$BUILDOUT_INSTALL_SERVER_DEV

echo "*******************"
echo "***   Testing   ***"
echo "*******************"
$BUILDOUT_TEST
TEST_RC=$?

echo "*********************"
echo "***   Analytics   ***"
echo "*********************"
$BUILDOUT_COVERAGE
echo "Completed coverage"
$BUILDOUT_LINT $PROJECT_NAME > logs/pylint.xml
echo "Completed lint"

if [[ $TEST_RC -eq 0 ]] 
then
    echo "*********************"
    echo "***   Deploying   ***"
    echo "*********************"
    rm -fr $TARGET
    mkdir $TARGET
    rsync -a --exclude-from=$SOURCE/etc/excludes.txt $SOURCE/ $TARGET
    cd $TARGET
    $BUILDOUT_BOOTSTRAP
    $BUILDOUT_INSTALL_SERVER_INT
    $BUILDOUT_MINIFY
    $EXECUTE "chown -R webapp:apache $TARGET"
    $EXECUTE "chmod -R g+w $TARGET"
    $EXECUTE "chmod -R ugo+x $TARGET/bin/"
fi

echo "***********************"
echo "***   Script Done   ***"
echo "***********************"
exit 0

                                     