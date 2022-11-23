# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import action_pb2, action_pb2_grpc
from enum import Enum


class ActionResult:
    """ Generated by dcsdkgen """

    
    
    class Result(Enum):
        """ Generated by dcsdkgen """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        COMMAND_DENIED_LANDED_STATE_UNKNOWN = 6
        COMMAND_DENIED_NOT_LANDED = 7
        TIMEOUT = 8
        VTOL_TRANSITION_SUPPORT_UNKNOWN = 9
        NO_VTOL_TRANSITION_SUPPORT = 10
        PARAMETER_ERROR = 11

        def translate_to_rpc(self, rpcResult):
            rpcResult = {
                    0: action_pb2.ActionResult.UNKNOWN,
                    1: action_pb2.ActionResult.SUCCESS,
                    2: action_pb2.ActionResult.NO_SYSTEM,
                    3: action_pb2.ActionResult.CONNECTION_ERROR,
                    4: action_pb2.ActionResult.BUSY,
                    5: action_pb2.ActionResult.COMMAND_DENIED,
                    6: action_pb2.ActionResult.COMMAND_DENIED_LANDED_STATE_UNKNOWN,
                    7: action_pb2.ActionResult.COMMAND_DENIED_NOT_LANDED,
                    8: action_pb2.ActionResult.TIMEOUT,
                    9: action_pb2.ActionResult.VTOL_TRANSITION_SUPPORT_UNKNOWN,
                    10: action_pb2.ActionResult.NO_VTOL_TRANSITION_SUPPORT,
                    11: action_pb2.ActionResult.PARAMETER_ERROR
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: ActionResult.Result.UNKNOWN,
                    1: ActionResult.Result.SUCCESS,
                    2: ActionResult.Result.NO_SYSTEM,
                    3: ActionResult.Result.CONNECTION_ERROR,
                    4: ActionResult.Result.BUSY,
                    5: ActionResult.Result.COMMAND_DENIED,
                    6: ActionResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN,
                    7: ActionResult.Result.COMMAND_DENIED_NOT_LANDED,
                    8: ActionResult.Result.TIMEOUT,
                    9: ActionResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN,
                    10: ActionResult.Result.NO_VTOL_TRANSITION_SUPPORT,
                    11: ActionResult.Result.PARAMETER_ERROR,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ActionResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two ActionResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActionResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ActionResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ActionResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActionResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActionResult(
                
                ActionResult.Result.translate_from_rpc(rpcActionResult.result),
                
                
                rpcActionResult.result_str
                )

    def translate_to_rpc(self, rpcActionResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.result.translate_to_rpc(rpcActionResult.result)
            
        
        
        
            
        rpcActionResult.result_str = self.result_str
            
        
        



class ActionError(Exception):
    """ Raised when a ActionResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Action(AsyncBase):
    """ Generated by dcsdkgen - MAVSDK Action API """

    # Plugin name
    name = "Action"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = action_pb2_grpc.ActionServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ActionResult.translate_from_rpc(response.action_result)
    

    async def arm(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.ArmRequest()
        response = await self._stub.Arm(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "arm()")
        

    async def disarm(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.DisarmRequest()
        response = await self._stub.Disarm(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "disarm()")
        

    async def takeoff(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.TakeoffRequest()
        response = await self._stub.Takeoff(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "takeoff()")
        

    async def land(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.LandRequest()
        response = await self._stub.Land(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "land()")
        

    async def reboot(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.RebootRequest()
        response = await self._stub.Reboot(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "reboot()")
        

    async def kill(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.KillRequest()
        response = await self._stub.Kill(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "kill()")
        

    async def return_to_launch(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.ReturnToLaunchRequest()
        response = await self._stub.ReturnToLaunch(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "return_to_launch()")
        

    async def transition_to_fixed_wing(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.TransitionToFixedWingRequest()
        response = await self._stub.TransitionToFixedWing(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "transition_to_fixed_wing()")
        

    async def transition_to_multicopter(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.TransitionToMulticopterRequest()
        response = await self._stub.TransitionToMulticopter(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "transition_to_multicopter()")
        

    async def get_takeoff_altitude(self):
        """ Generated by dcsdkgen

        :returns: requested value
        """

        request = action_pb2.GetTakeoffAltitudeRequest()
        response = await self._stub.GetTakeoffAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_takeoff_altitude()")
        

        return response.altitude
        

    async def set_takeoff_altitude(self, altitude):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.SetTakeoffAltitudeRequest()
        request.altitude = altitude
        response = await self._stub.SetTakeoffAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_takeoff_altitude()", altitude)
        

    async def get_maximum_speed(self):
        """ Generated by dcsdkgen

        :returns: requested value
        """

        request = action_pb2.GetMaximumSpeedRequest()
        response = await self._stub.GetMaximumSpeed(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_maximum_speed()")
        

        return response.speed
        

    async def set_maximum_speed(self, speed):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.SetMaximumSpeedRequest()
        request.speed = speed
        response = await self._stub.SetMaximumSpeed(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_maximum_speed()", speed)
        

    async def get_return_to_launch_altitude(self):
        """ Generated by dcsdkgen

        :returns: requested value
        """

        request = action_pb2.GetReturnToLaunchAltitudeRequest()
        response = await self._stub.GetReturnToLaunchAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_return_to_launch_altitude()")
        

        return response.relative_altitude_m
        

    async def set_return_to_launch_altitude(self, relative_altitude_m):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        request = action_pb2.SetReturnToLaunchAltitudeRequest()
        request.relative_altitude_m = relative_altitude_m
        response = await self._stub.SetReturnToLaunchAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_return_to_launch_altitude()", relative_altitude_m)
        