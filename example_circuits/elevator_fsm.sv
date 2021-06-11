`timescale 1ns / 1ps
module elevator_fsm(
    input clk,
    input rst,
    input door_open_req,
    input door_close_req,
    input [1:0] car_floor_req,
    input floor_1_cab_req,
    input floor_2_cab_req,
    input [1:0] floor_sensor,
    output reg cmd_door_open,
    output reg cmd_door_close,
    output reg cmd_car_up,
    output reg cmd_car_down
    );
    parameter IDLE = 4'b0001;
    parameter DOORS_OPEN = 4'b0010;
    parameter DOORS_OPEN_COUNT_DOWN = 4'b0100;
    parameter DOORS_CLOSE = 4'b1000;
    parameter [7:0] DOORS_OPEN_TIME = 10;
    reg [3:0] state;
    reg [7:0] door_close_timer;
    reg [3:0] next_state;
    always_ff @(posedge clk) begin
        if (~rst) begin
            state <= IDLE;
            door_close_timer = 0;
        end
        else begin
            state <= next_state;
        end 
    end
    always_comb begin
        case (state)
            IDLE: begin
                if (door_open_req) begin
                    next_state = DOORS_OPEN;
                end
                else if (door_close_req) begin
                    next_state = DOORS_CLOSE;
                end
                else begin
                    next_state = IDLE;
                end
            end
            DOORS_OPEN: begin
                if (door_open_req) begin
                    next_state = DOORS_OPEN;
                end
                else begin
                    next_state = DOORS_OPEN_COUNT_DOWN;
                end
            end
            DOORS_OPEN_COUNT_DOWN: begin
                if (door_close_timer == 0) begin
                    next_state = DOORS_CLOSE;
                end
                else begin
                    next_state = DOORS_OPEN_COUNT_DOWN;
                end
            end
            DOORS_CLOSE: begin
                next_state = IDLE;
            end
        endcase
    end
    always_ff @(posedge clk) begin
        case (next_state)
            IDLE: begin
                cmd_door_open <= 0;
                cmd_door_close <= 1;
                cmd_car_up <= 0;
                cmd_car_down <= 0;
            end
            DOORS_OPEN: begin
                cmd_door_open <= 1;
                cmd_door_close <= 0;
                cmd_car_up <= 0;
                cmd_car_down <= 0;
                door_close_timer <= DOORS_OPEN_TIME;
            end
            DOORS_OPEN_COUNT_DOWN: begin
                cmd_door_open <= 1;
                cmd_door_close <= 0;
                cmd_car_up <= 0;
                cmd_car_down <= 0;
                door_close_timer <= door_close_timer - 1;
            end
            DOORS_CLOSE: begin
                cmd_door_open <= 0;
                cmd_door_close <= 1;
                cmd_car_up <= 0;
                cmd_car_down <= 0;
            end
        endcase
    end
endmodule
