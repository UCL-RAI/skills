# Robotics Code Checks

## Frames and Units

- Coordinate frames are named and documented.
- Units are explicit for distance, angle, velocity, torque, time, and frequency.
- Transform direction is not ambiguous.
- Timestamp assumptions are visible.
- Quaternion/Euler conventions and axis order are explicit when relevant.
- Sensor frame, robot base frame, world/map frame, and object frame are not conflated.

## Simulation and Hardware

- Simulator version and model assets are traceable.
- Sim-only assumptions are stated.
- Hardware safety constraints are not bypassed.
- Control-loop frequency and latency are checked where relevant.
- Physical limits, joint bounds, velocity/torque limits, and emergency stop assumptions are visible.
- Domain randomization, noise, contact/friction, and dynamics assumptions are documented when they affect claims.

## ML and Experiments

- Seeds, configs, checkpoints, and logs are captured.
- Dataset versions and splits are traceable.
- Evaluation scripts can be rerun.
- Reported metrics match saved artifacts.
- Train/validation/test leakage is considered.
- Preprocessing, normalization, and augmentation are identical between training and evaluation unless intentionally changed.
- Statistical reporting matches the claim strength.

## ROS and C++

- Launch/config files match code defaults.
- Topic, service, and action names are stable.
- Python/C++ interfaces have clear ownership and error handling.
- Build/test commands are documented or discoverable.
- Message timestamps and QoS/queue assumptions are compatible with consumers.
- Node lifecycle, parameters, namespaces, and remappings are not silently changed.

## Reproducibility and Packaging

- Commands to reproduce the result are recorded.
- Environment, dependency, simulator, and dataset versions are discoverable.
- Generated artifacts are not confused with source files.
- Large files, credentials, and machine-local paths are not committed.

## Review Severity Examples

- `blocking`: unsafe hardware behavior, incorrect frame transform, fabricated metric, data leakage, or non-reproducible core result.
- `major`: missing test around critical behavior, weak error handling at Python/C++ boundary, undocumented config change, or simulator assumption that invalidates a claim.
- `minor`: local clarity, missing comment around non-obvious robotics convention, or incomplete logging.
- `nit`: formatting, naming, or low-risk readability issue.
