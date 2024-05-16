#!/bin/bash

helmfile template --include-crds > "helmed-$(basename "$PWD").yaml"
