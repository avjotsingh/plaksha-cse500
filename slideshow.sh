#!/bin/bash
jupyter nbconvert plaksha/Lectures/Lecture${1}.ipynb --to slides --post serve --ServePostProcessor.ip='*'
