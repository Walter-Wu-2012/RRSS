import sktime

# TODO: modify the data format
# step 1: data specification
y = load_airline() # mood index
# we create some dummy exogeneous data
X = pd.DataFrame(index=y.index) # event stimulus

# step 2: specifying forecasting horizon
# prediction range 12 hours
fh = np.arange(1, 12)

# step 3: specifying the forecasting algorithm
forecaster = NaiveForecaster(strategy="last", sp=12)

# step 4: fitting the forecaster
forecaster.fit(y, X=X, fh=fh)

# step 5: querying predictions
y_pred = forecaster.predict(X=X)