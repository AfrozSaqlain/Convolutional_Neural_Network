# A guide to Files
- `gen.py` orr `gen_with_additional_functionalities.py`: This is used to generate qtransform spectrograms of synthetic GW signals assuming aLIGO sensitivity. Sampling frequency is 4096 Hz.
- `tranformer.py` and `cnn.ipynb`: These are the neural network code where I have defined the model's structure and done training and testing.
- `transformer_with_ROC_and_File_Classification.py`: This not only trains the model but alsos generates ROC curve, AUC score, and also tells which data were wrongly classified, and stores that as an additional information in `misclassified_{}.txt` file.

# How GW waveforms are generated

We use `TEOBResumS` to generate signals assuming `f_lower` = 5. Two sets of data are generated: 
- Eccentric: By giving the `eccentricity` parameter, sampled from prior assuming `Uniform` distribution in [0.1, 0.6].
- Non-Eccentric: By giving the `eccentricity` parameter value to be equal to 0.

The Non-Eccentric waveform is then used to generate unlensed data as well as lensed data. Lensing is done using `GWMAT` package.

The waveforms are then projected onto `H1` detector by using `ra`, `dec`, and `polarization` values sampled from the prior

Each wave is then tapered. Then we generated noise from `aLIGOZeroDetHighPower` PSD.

Next we pad each GW signal and add it to the noise such that the peak of the signal lies within 2.2 seconds to 2 seconds window before the noise ends. This is done to make the training process robust to moderate time
translations in the signal.

We also ensure that the signal's SNR is always greater than a minimum threshold, i.e. 10 by multiplying the signal by a sampled `scale_factor`.

The signal is then cropped so that the data is of 8s duration.

Then finally we generate the `q_transforms` of each signal and save them as `PNG` file with naming convention such that if the signal is `lensed` then the name of the file is `lensed_{num},png`, where `num` just represnts file number.

## 📋 Prior Distributions Table

| **Parameter**   | **Distribution Type**              | **Range / Description**       |
|------------------|------------------------------------|-------------------------------|
| `mass1`         | `Constraint`                       | [10, 100]                     |
| `mass2`         | `Constraint`                       | [10, 100]                     |
| `mass_ratio`    | `UniformInComponentsMassRatio`     | [0.2, 10]                     |
| `chirp_mass`    | `UniformInComponentsChirpMass`     | [25, 100]                     |
| `spin1z`        | `Uniform`                          | [0.0, 0.9]                    |
| `spin2z`        | `Uniform`                          | [0.0, 0.9]                    |
| `eccentricity`  | `Uniform`                          | [0.1, 0.6]                    |
| `coa_phase`     | `Uniform`                          | [0.0, 2π]                     |
| `distance`      | `Uniform`                          | [100, 1000]                   |
| `dec`           | `Cosine`                           | [−π/2, π/2]                   |
| `ra`            | `Uniform` (periodic)               | [0, 2π]                       |
| `polarization`  | `Uniform` (periodic)               | [0, π]                        |
| `Log_Mlz`       | `Uniform`                          | [3, 5]                        |
| `yl`            | `PowerLaw` (`α = 1`)               | [0.01, 1.0]                   |


**Note:** The `gen_with_additional_functionalities.py` code also generates a Lookup table for SNR values and parameter values corresponding to each sample and each category. Also sample `data` generated is given in `data_for_reference` folder alongwith its `SNR Lookup Table` as well as `Parameter Reference` in csv format.