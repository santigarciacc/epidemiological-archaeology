# Epidemics V2.10 final reproducibility snapshot

Final computational snapshot for the Epidemics submission. It preserves the audited national COVID-19 analysis and source-linked 1918 reconstruction.

- Primary estimand: epidemic-wave timing and geometry.
- Conditional estimand: infection-equivalent amplitude under explicit IFR/EFR scenarios.
- 1918 rows share a common Jan 1918-May 1919 calendar.
- U.S. March-May Army respiratory activity is a chronology sentinel, not a national civilian infection estimate.

Run `bash reproducibility/run_all.sh` for the full frozen pipeline.

## Final 1918 chronology correction
The U.S. first wave is displayed from observed U.S. Army respiratory morbidity in March-May 1918. Across 37 large Army camps, 143,986 of 1,219,359 personnel (11.8%) were hospitalized for respiratory illness during March-May. This precedes the first widely reported Spanish outbreak in Madrid on 22 May 1918. The Army series is used as observed morbidity/chronology and is not converted into a national civilian infection estimate.

## Portability

The workflow is portable at the level of computational architecture and decision rules: the same regularization, wave extraction, timing comparison, and audit logic is used across heterogeneous national COVID-19 mortality series and the historical 1918 stress test. Disease-specific delay and IFR/EFR parameters are not assumed to be universal and must be re-specified for each setting.
