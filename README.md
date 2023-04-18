# Remaster
## Main Goal
To extend the study done during my master's degree, now without time limitations and with more freedom of techniques.

## Points that make the original project complex and difficult to study
1. Dataset too large. With data from all over Norway, any training iteration is very costly and time consuming.
2. As it is an academic master's work, it was necessary to have a specific approach indicated by the supervisor professor to maintain the focus of the work. However, the objective now will not be to "lose focus", but to calmly analyze more points that may be interesting with the available data

## Steps that need to be done
1. Filter the original dataset to Oslo surroundings only.
2. Create map view with stations to illustrate the area of interest.
3. Explore other ways to do preprocessing. Take out outliers from the base (it can be either extreme temperatures or extreme errors). I think it's interesting not to use OHE.
4. Train models with hyperparameter optimization starting with what was done in the master's degree
    * MLP
    * CNN
    * RandomForest
    * XGBoost
    * GCN and other Graph Networks
