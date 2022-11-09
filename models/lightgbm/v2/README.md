# meshlearn model "v2"

## Overview

A model to predict local gyrification index on FreeSurfer brain meshes.

* RMSE on test set: 0.0163 (less is better)
* Trained on 384 files with 50k samples per file (19.8M observations), with neighborhood size 100 and radius 10mm.


## Suitable meshlearn software version

* This was created with [meshlearn](https://github.com/dfsp-spirit/meshlearn) version tagged: [v2_lgbm_flaml](https://github.com/dfsp-spirit/meshlearn/releases/tag/v2_lgbm_flaml)
* Full export of used conda environment: [environment_exported.yml](./environment_exported.yml)
* Model information: see model JSON file in this directory.
