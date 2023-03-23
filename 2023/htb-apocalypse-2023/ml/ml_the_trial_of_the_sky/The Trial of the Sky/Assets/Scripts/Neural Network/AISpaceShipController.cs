using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class AISpaceShipController : MonoBehaviour
{
    public NeuralNetwork network = null;

    public SpaceShipController controller;
    private Vector3 lastPosition;
    public float timeElapsed;
    private float avgSensor;
    public bool alive = true;


    void Start(){
        timeElapsed = 0;
        lastPosition = this.controller.spaceship.position;
    }

    void Update(){
        if (alive)
        {
            
            List<double> input = new List<double>();
            for (int i = 0; i < controller.sensors.Count; i++)
            {
                input.Add(controller.sensors[i].hitNormal);
            }
            input.Add(controller.speed / controller.acceleration);

           
            double[] output = network.Run(input);

          
            controller.spaceshipTurn = (float)output[0];
            controller.spaceshipDrive = (float)output[1];

            if (controller.playerHitWall)
            {
                int last_checkpoint = controller.spaceshipCheckPoint.nextCheckpoint;
                Debug.Log("The spaceship crashed before reaching checkpoint " + last_checkpoint);
                Stop();
            }
            if (controller.playerStopped)
            {
                Stop();
            }
        }
    }


    public void Stop(){
        alive = false;
        controller.spaceshipTurn = 0;
        controller.spaceshipDrive = 0;
        controller.spaceship.isKinematic = true;
        controller.spaceship.velocity = Vector3.zero;
    }

    public void Reset(Vector3 startingPos, Quaternion rotation)
    {
        this.controller.ResetPosition(startingPos, rotation);
        alive = true;
        controller.spaceship.isKinematic = false;
    }
}
