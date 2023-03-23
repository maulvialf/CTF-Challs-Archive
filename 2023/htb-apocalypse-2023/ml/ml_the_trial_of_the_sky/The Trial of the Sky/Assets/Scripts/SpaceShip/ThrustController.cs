using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThrustController : MonoBehaviour{
    Vector3 thrusterAngle;
    float steerAngle, maxSteerAngle = 30f;
    public Rigidbody2D spaceship;
    public SpaceShipController aispaceship;
    // Update is called once per frame
    void Update(){
        steerAngle = maxSteerAngle * aispaceship.spaceshipTurn + spaceship.rotation;
    }

    void LateUpdate(){

        thrusterAngle = transform.eulerAngles;
        thrusterAngle.z = steerAngle;
        transform.eulerAngles = thrusterAngle;
    }
}
