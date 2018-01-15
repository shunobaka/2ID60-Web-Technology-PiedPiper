import {Component, OnInit} from '@angular/core'
import {MessageService} from '../services/message.service';
import {Message} from "../models/message";
import {UserService} from "../services/user.service";
import {User} from "../models/user";

@Component({
  selector: 'app-chat-room',
  templateUrl: './chat-room.component.html',
  styleUrls: ['./chat-room.component.css']
})

export class ChatRoomComponent {
  profileImage: string;
  profileName: string;
  inChat: boolean;
  messages: Message[];
  token: string;

  constructor(
    private messageService: MessageService,
    private userService: UserService) {
  }
}
