import {
    Entity,
    Column,
    PrimaryGeneratedColumn,
  } from 'typeorm';
  
  @Entity()
  export class UserKey {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    name: string;
  
    @Column()
    key: string;
  }
  