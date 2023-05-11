#!/bin/bash
for p in ./*.png; do rm "$p"; done
for r in ./*.raw; do rm "$r"; done
for r in ./raw/*; do rm "$r"; done
for w in ./*.wav; do rm "$w"; done