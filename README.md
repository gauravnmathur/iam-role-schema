# iam-role-schema

## Schema Files
```
schema-iam-role.json
schema-role-actions.json
schema-role-allowed_types.json
```

## Example Runs
### Example of valid schema verification

```
>> python validate_role.py schema-iam-role.json examples/feed-admin-valid.json
```

### Example #1 if invalid schema

```
>> python validate_role.py schema-iam-role.json examples/feed-admin-invalid1.json
u'feed:badAction' is not one of [u'feed:deleteFlow', u'taas:getStop', u'taas:removeVehicles', u'deployments:getDeviceHistory', u'iam:createPermission', u'deployments:cancelVehicleDeployment', u'vehicle:getStatus', u'taas:assignServiceAreaStops', u'resources:listDevices', u'vehicle:getActuation', u'billing:attribute', u'deployments:getReleaseArtifact', u'feed:getTap', u'taas:removeInstance', u'taas:addStops', u'taas:updateStop', u'vsdn:updateFuelTankPart', u'taas:listInstances', u'taas:arriveAtVehicleWaypoints', u'deployments:createRelease', u'taas:listVehicles', u'taas:getRide', u'deployments:getVehicleHistory', u'iam:deletePermission', u'taas:acceptVehicleWaypoints', u'vehicle:getPermission', u'taas:updateRide', u'taas:addVehicles', u'taas:acceptRideOffer', u'taas:removeStops', u'taas:listServiceAreaVehicles', u'feed:listFlows', u'feed:readTelemetry', u'taas:updateVehicle', u'deployments:getVehicleDeploymentDescription', u'device:actuateDevice', u'deployments:getDeployment', u'taas:completeVehicleWaypoints', u'deployments:createDeployment', u'resources:getDevice', u'iam:listPermissions', u'deployments:createTargetBundle', u'taas:listVehicleAssignments', u'taas:createInstance', u'taas:getServiceArea', u'taas:assignServiceAreaVehicles', u'deployments:getDeviceQueue', u'deployments:createArtifact', u'vsdn:deleteHvbom', u'taas:unassignServiceAreaStops', u'resources:listVehicles', u'taas:reassignRides', u'resources:updateVehicleTags', u'deployments:getTargetBundle', u'resources:deleteDevice', u'taas:cancelRide', u'feed:listTapsToFlow', u'iam:deleteUser', u'vehicle:listPermissions', u'taas:getProcess', u'resources:createDevice', u'taas:getVehicle', u'feed:readFlow', u'resources:upsertDevice', u'taas:updateInstance', u'resources:updateDeviceTags', u'deployments:getDeviceDeploymentDescription', u'taas:listStops', u'resources:listVehicleBindings', u'vehicle:createActuation', u'taas:removeServiceArea', u'taas:unassignServiceAreaVehicles', u'vsdn:addFuelTankPart', u'taas:updateServiceArea', u'taas:listServiceAreaStops', u'resources:listDeviceBindings', u'deployments:cancelDeviceDeployment', u'deployments:cancelDeployment', u'resources:getVehicle', u'feed:createTapFromFlow', u'feed:createFlow', u'iam:createUser', u'feed:editTap', u'resources:createVehicle', u'resources:upsertVehicle', u'deployments:getRelease', u'taas:createServiceArea', u'taas:listServiceAreas', u'vehicle:createPermission', u'taas:requestRide', u'iam:listUsers', u'deployments:deployRelease', u'taas:getInstance', u'vehicle:listActuations', u'taas:listRides', u'feed:deleteTap', u'vehicle:deletePermission', u'iam:getPermission', u'resources:deleteVehicle']

Failed validating u'enum' in schema[u'properties'][u'statements'][u'items'][u'properties'][u'actions'][u'items']:
...

```

### Example #2 of invalid schema
```
>> python validate_role.py schema-iam-role.json examples/feed-admin-invalid2.json
Additional properties are not allowed (u'extraField' was unexpected)

Failed validating u'additionalProperties' in schema[u'properties'][u'statements'][u'items']:
...
```

### Example #3 of invalid schema

```
>> python validate_role.py schema-iam-role.json examples/feed-admin-invalid3.json
u'this-type-is-invalid' is not one of [u'lock', u'*', u'aui:iam:role/deployment-manager', u'aui:iam:role/feed-admin', u'aui:iam:role/feed-reader', u'unlock', u'startIgnition', u'stopIgnition', u'aui:iam:role/vehicle-owner']

Failed validating u'enum' in schema[u'properties'][u'statements'][u'items'][u'properties'][u'allowed_types'][u'items']:

```
