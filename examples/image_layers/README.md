# Image Layers

This example shows that docker caches all layers until the first command that cannot be cached.

The conclusion is that you need to push things that change often *down* your Dockerfile and things
that change *rarely* up your Dockerfile to achieve fast building times of images.
