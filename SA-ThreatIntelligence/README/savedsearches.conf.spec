
###### nbtstat ######
action.nbtstat = [0|1]
    * Enable nbtstat action
    
action.nbtstat.param.host_field = <string>
    * The name of the field representing the value to perform a nbtstat scan on
    * Defaults to None.
    
action.nbtstat.param.max_results = <int>
    * The number of results to perform a nbtstat scan on
    * Each field value counts as a result
    * Defaults to 1.
    

###### notable ######
action.notable = [0|1]
    * Enable notable action


###### nslookup ######
action.nslookup = [0|1]
    * Enable nslookup action
    
action.nslookup.param.host_field = <string>
    * The name of the field representing the value to perform a nslookup scan on
    * Defaults to None.
    
action.nslookup.param.max_results = <int>
    * The number of results to perform a nslookup scan on
    * Each field value counts as a result
    * Defaults to 1.
    

###### ping ######
action.ping = [0|1]
    * Enable ping action
    
action.ping.param.host_field = <string>
    * The name of the field representing the value to perform a ping scan on
    * Defaults to None.
    
action.ping.param.max_results = <int>
    * The number of results to perform a ping scan on
    * Each field value counts as a result
    * Defaults to 1.


###### risk ######
action.risk = [0|1]
    * Enable risk action

action.risk.param._risk_score  = <int>
    * The score to apply to risk modifiers generated by the implementation of this action
    * Defaults to 1

action.risk.param._risk_object = <string>
    * The field name to use as the risk_object
    * Field must be available in the result set passed to this action
    * Defaults to None

action.risk.param._risk_object_type = [system|user|<string>|other]
    * The type of risk_object
    * Must be one of "system", "user", arbitrary string, or "other"
    * <string> allows for type extensions
    * Defaults to None
